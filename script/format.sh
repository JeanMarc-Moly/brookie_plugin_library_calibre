#!/bin/sh
isort ${APP}
black ${APP}
isort test
black test
