


# FFMPEG https://ffmpeg.org/ffmpeg-filters.html#tile
ffmpeg -loop 1 -t 1 -i e103.png -filter_complex tile=5x5:margin=5:padding=5:color=white output.png

ffmpeg -loop 1 -t 1 -i e103.png -filter_complex tile=5x1:margin=5:padding=5:color=white output.png

# Imagemagick

magick montage -mode concatenate -tile 4x e103.png rejoined.png

# Method 1
```
magick montage e103.png +clone +clone +clone -tile x1 -border 5 -geometry +0+0 temp/row1.png
magick montage e103.png +clone +clone +clone -tile x1 -border 5 -geometry +0+0 temp/row2.png
magick montage e103.png +clone +clone +clone -tile x1 -border 5 -geometry +0+0 temp/row3.png
magick montage e103.png +clone +clone +clone -tile x1 -border 5 -geometry +0+0 temp/row4.png

ffmpeg -loop 1 -t 1 -i temp/row%d.png -filter_complex tile=4x1:margin=5:padding=5:color=white output.png
```

# Simple method (working)
magick montage  temp/row1.png temp/row6.png temp/row6.png  -tile x3  -geometry +0+0  out.png
magick montage  out.png  +clone +clone +clone -tile x1  -geometry +0+0  out2.png


magick montage  wall/FISH-A.jpg wall/FISH-A.jpg wall/FISH-HL.jpg  wall/FISH-C.jpg wall/FISH-C.jpg wall/FISH-C.jpg -tile x6  -border 1 -geometry +0+0  out.png

magick montage  out.png  +clone +clone +clone -tile x1  -geometry +0+0  out2.png

# Image prespective 
https://stackoverflow.com/questions/9686803/imagemagick-skew-or-distort-an-image

magick out2.png -background none -virtual-pixel background +distort Perspective "0,0 0,0  400,0 400,22  400,300 400,320  0,300 0,300" out3.png

magick out2.png -background none -virtual-pixel background +distort Perspective "0,0 541,286  0,%[fx:h-1] 82,542  %[fx:w-1],%[fx:h-1] 1137,549  %[fx:w-1],0 1306,203" out3.png

## Imagemagick canvas compissite 

https://github.com/ImageMagick/ImageMagick/discussions/5305

## HTML Canvas 

https://stackoverflow.com/questions/52025966/drawing-the-floor-tiles-with-angles-using-canvas-html5
https://www.geeksforgeeks.org/css-perspective-function/
https://github.com/wanadev/perspective.js

http://fabricjs.com/
  http://jsfiddle.net/m1erickson/Rq7hk/

threejs.com
  https://stackoverflow.com/questions/49987322/perspective-transformation-of-image-using-three-js
  https://github.com/jlouthan/perspective-transform

Canvas load from file: http://jsfiddle.net/t7mv6/86/

## Imagemagick 

### composite: 
-> https://legacy.imagemagick.org/Usage/layers/#composite
-> https://github.com/ImageMagick/ImageMagick/discussions/5305

magick -size 1920x1080 xc:skyblue image/bg/room-3.png -composite out/outtext.png
  
magick out/DN-1031.png { image/bg/room-3.png -gravity Center -crop 1920:890+0+0 +repage -resize "1920x890^!" } -gravity northwest -geometry +310+77 -composite out/out3.jpg

magick -size -1920x1080 xc:skyblue  { out/DN-1031.png -crop 1920x890+0+0 +repage } -gravity northwest -geometry +0+0 -composite out/out3.jpg

magick -size 1920x1080 xc:skyblue { out/DN-1031.png -crop 1920x890+0+0 +repage } -composite out/out4.png

# Working steps 

magick out/DN-1031.png -resize 1920x890^ -crop 1920x890+0+0 out/out5.png

magick out/DN-1031.png -gravity northwest -resize 1920x890^ -crop 1920x890+0+0 out/out5.png

magick -size 1920x1080 xc:ivory  out/out5.png -gravity northwest -geometry +0+0 -composite image/bg/room-3.png -composite out/out6.png

magick -size 1920x1080 xc:ivory  { out/DN-1031.png -resize 1920x890^ -crop 1920x890+0+0 } -gravity northwest -geometry +0+0 -composite image/bg/room-3.png -composite out/out6.png


magick montage out/temp.png  -size 1920x890 tile:out/temp.png  out/DN-1031.png

magick montage out/temp.png -border 0 -geometry 1920x -tile x1 out/final.png


magick montage  out/temp.png +clone +clone -tile x1 -geometry +0+0 out/out2.png

magick out/temp.png -roll +0+135 out/_orange_270_r.jpg
magick montage out/temp.png +clone +clone +clone -tile x4 -geometry +0+0 out/_1col.png

# From openai
magick montage input_image.jpg -tile 2x2 -geometry +10+10 -background black -mode Concatenate -resize 600x400 output_image.jpg

magick montage  .\out\temp.png  -duplicate 4 -tile x1  -geometry +0+0 out/tee.png


magick out/DN-1031.png -gravity southwest -resize 1920x890^ -crop 1920x890+0+0 out/out5.png
magick -size 1920x1080 xc:darkgrey  out/out5.png -gravity northwest -geometry +0+0 -composite image/bg/room-3.png -composite out/out6.png

magick -size 1920x1080 xc:darkgrey  out/temp_level_3.png -gravity northwest -geometry +0+0 -composite image/bg/room-3.png -composite out/out7.png
