


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