#!/usr/bin/env sh
export $(grep -v '^#' kaggle.env | xargs)