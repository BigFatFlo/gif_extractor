#! /bin/sh
gimp -i -b "(convert-to-gif $1 \"$2\" \"$3\" \"$4\")" -b '(gimp-quit 0)'