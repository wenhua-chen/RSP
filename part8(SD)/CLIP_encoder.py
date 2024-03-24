# CLIP文本编码

from transformers import CLIPTextModel, CLIPTokenizer

# 加载 CLIP Text Encoder模型和Tokenizer
# SD V1.5模型权重百度云网盘：关注Rocky的公众号WeThinkIn，后台回复：SDV1.5模型，即可获得资源链接
text_encoder = CLIPTextModel.from_pretrained("/本地路径/stable-diffusion-v1-5", subfolder="text_encoder").to("cuda")
text_tokenizer = CLIPTokenizer.from_pretrained("/本地路径/stable-diffusion-v1-5", subfolder="tokenizer")

# 将输入SD模型的prompt进行tokenize，得到对应的token ids特征
prompt = "1girl,beautiful"
text_token_ids = text_tokenizer(
    prompt,
    padding="max_length",
    max_length=text_tokenizer.model_max_length,
    truncation=True,
    return_tensors="pt"
).input_ids

print("text_token_ids' shape:",text_token_ids.shape)
print("text_token_ids:",text_token_ids)

# 将token ids特征输入CLIP Text Encoder模型中输出77x768的Text Embeddings特征
text_embeddings = text_encoder(text_token_ids.to("cuda"))[0] # 由于CLIP Text Encoder模型输出的是一个元组，所以需要[0]对77x768的Text Embeddings特征进行提取
print("text_embeddings' shape:",text_embeddings.shape)
print(text_embeddings)