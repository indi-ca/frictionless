#!/bin/bash


SOURCE=frictionless.design.png
TARGET=../layouts/osx/frictionless.ukelele.icns

rm -rf Frictionless.iconset
mkdir Frictionless.iconset

convert $SOURCE -resize x16 Frictionless.iconset/icon_16x16.png
convert $SOURCE -resize x32 Frictionless.iconset/icon_16x16@2x.png
convert $SOURCE -resize x32 Frictionless.iconset/icon_32x32.png
convert $SOURCE -resize x64 Frictionless.iconset/icon_32x32@2x.png
convert $SOURCE -resize x128 Frictionless.iconset/icon_128x128.png
convert $SOURCE -resize x128 Frictionless.iconset/icon_128x128@2x.png
convert $SOURCE -resize x256 Frictionless.iconset/icon_256x256.png
convert $SOURCE -resize x512 Frictionless.iconset/icon_256x256@2x.png
convert $SOURCE -resize x512 Frictionless.iconset/icon_512x512.png
convert $SOURCE -resize x1024 Frictionless.iconset/icon_512x512@2x.png

iconutil -c icns -o Frictionless.icns Frictionless.iconset

#rm ../layouts/osx/frictionless.ukelele.icns
mv Frictionless.icns $TARGET
