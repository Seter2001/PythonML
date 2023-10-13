{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOqhv+BqII2uSXeJ/1t8IE0",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Seter2001/PythonML/blob/master/triangle.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "id": "BiEERgsB0Z4C"
      },
      "outputs": [],
      "source": [
        "def triangle(a,b,c):\n",
        "  if a + b > c and a + c > b and b + c > a:\n",
        "    return True\n",
        "  else:\n",
        "    return False"
      ]
    }
  ]
}