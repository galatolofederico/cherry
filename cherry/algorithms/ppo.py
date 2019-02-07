#!/usr/bin/env python3

import torch as th

"""
    * TODO: validate of all variables so as to explicitly fail.
"""


def policy_loss(new_log_probs, old_log_probs, advantages, clip=0.1):
    ratios = th.exp(new_log_probs - old_log_probs)
    obj = ratios * advantages
    obj_clip = ratios.clamp(1.0 - clip, 1.0 + clip) * advantages
    return - th.min(obj, obj_clip).mean()


def value_loss(new_values, old_values, rewards, clip=0.1):
    loss = (rewards - new_values)**2
    clipped_values = old_values + (new_values - old_values).clamp(-clip, clip)
    clipped_loss = (rewards - clipped_values)**2
    return 0.5 * th.max(loss, clipped_loss).mean()
