# VAE进行图片的encode, 然后再decode, 观察VAE的效果

import cv2
import torch
import numpy as np
from diffusers import AutoencoderKL

# 加载VAE模型: VAE模型可以通过指定subfolder文件来单独加载。
# SD V1.5模型权重百度云网盘：关注Rocky的公众号WeThinkIn，后台回复：SD模型，即可获得资源链接
VAE = AutoencoderKL.from_pretrained("/本地路径/stable-diffusion-v1-5", subfolder="vae")
VAE.to("cuda", dtype=torch.float16)

# 用OpenCV读取和调整图像大小
raw_image = cv2.imread("catwoman.png")
raw_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2RGB)
raw_image = cv2.resize(raw_image, (1024, 1024))

# 将图像数据转换为浮点数并归一化
image = raw_image.astype(np.float32) / 127.5 - 1.0

# 调整数组维度以匹配PyTorch的格式 (N, C, H, W)
image = image.transpose(2, 0, 1)
image = image[None, :, :, :]

# 转换为PyTorch张量
image = torch.from_numpy(image).to("cuda", dtype=torch.float16)

# 压缩图像为Latent特征并重建
with torch.inference_mode():
    # 使用VAE进行压缩和重建
    latent = VAE.encode(image).latent_dist.sample()
    rec_image = VAE.decode(latent).sample

    # 后处理
    rec_image = (rec_image / 2 + 0.5).clamp(0, 1)
    rec_image = rec_image.cpu().permute(0, 2, 3, 1).numpy()

    # 反归一化
    rec_image = (rec_image * 255).round().astype("uint8")
    rec_image = rec_image[0]

    # 保存重建后图像
    cv2.imwrite("reconstructed_catwoman.png", cv2.cvtColor(rec_image, cv2.COLOR_RGB2BGR))