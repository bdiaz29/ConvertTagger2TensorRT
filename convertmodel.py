import toml
import os
from tensorflow.keras.models import load_model
import tf2onnx
import onnx
import toml
import argparse


def relative_to_absolute(relative_path):
    # Get the current working directory of the Python script
    current_dir = os.getcwd()
    # Combine the current working directory with the relative path
    absolute_path = os.path.join(current_dir, relative_path)
    # Normalize the path to handle any path separators
    absolute_path = os.path.normpath(absolute_path)
    return absolute_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process folder')
    parser.add_argument('--batch_size', help='static batch size', required=True)
    parser.add_argument('--model_path', help='path to model', required=True)
    parser.add_argument('--name', help='oupur nme', required=True)
    args= parser.parse_args()
    data = toml.load('config.toml')
    trtexec_path = data['trtexec_path']
    name = args.name
    model_dir = args.model_path
    batch_size = int(float(args.batch_size))
    print("loading model")
    model = load_model(model_dir)
    model_proto, external_tensor_storage = tf2onnx.convert.from_keras(model,
                                                                      input_signature=None, opset=None, custom_ops=None,
                                                                      custom_op_handlers=None, custom_rewriter=None,
                                                                      inputs_as_nchw=None, outputs_as_nchw=None,
                                                                      extra_opset=None,
                                                                      shape_override=None, target=None,
                                                                      large_model=False,
                                                                      output_path=None)
    inputs = model_proto.graph.input
    for input in inputs:
        dim1 = input.type.tensor_type.shape.dim[0]
        dim1.dim_value = batch_size
    print("saving model as onnx")
    onnx.save_model(model_proto, r'tmp.onnx')
    tmp_absolute = relative_to_absolute('tmp.onnx')
    shellcommand = f'{trtexec_path} --onnx={tmp_absolute} --saveEngine={name}.trt'
    os.system(shellcommand)



