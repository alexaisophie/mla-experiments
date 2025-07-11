import torch

"""
RoPE taken from GPT-NeoX style, via llama in transformers.

References (this was way too hard to do without looking up substantially)

https://github.com/huggingface/transformers/issues/25199#issuecomment-1687720247

https://github.com/lucidrains/rotary-embedding-torch/tree/main
"""

def rotate_half_old(x):
    x1, x2 = x.chunk(2, dim=-1)
    return torch.cat((-x2, x1), dim=-1)

def rotate_half(x):
    x_even, x_odd = x[:, ::2], x[:, 1::2]
    return torch.stack([-x_odd, x_even], dim=-1).flatten(start_dim=-2, end_dim=-1)

def apply_rope(q, k, cos, sin):
    q = (q * cos) + (rotate_half(q) * sin)
    k = (k * cos) + (rotate_half(k) * sin)
    return q, k

def apply_rope_x(x, cos, sin):
    return (x * cos) + (rotate_half(x) * sin)

