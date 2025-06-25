import torch

print("Demo 31: Informacion Torch y Dispositivo de Salida")
versionTorch = torch.__version__
print("Version de PyTorch: ", versionTorch)
tieneCuda = torch.cuda.is_available()
print("Tiene CUDA: ", tieneCuda)
if(tieneCuda):
    versionActual = torch.cuda.current_device()
    print("Version Actual: ", versionActual)
    nombreGPU = torch.cuda.get_device_name(versionActual)
    print("Nombre GPU: ", nombreGPU)