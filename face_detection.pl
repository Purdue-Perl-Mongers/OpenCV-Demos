use strict;
use warnings;

use Image::ObjectDetect;

if($#ARGV < 0) {
	print "Path to image is required\n";
	exit;
}

# get path to image
my $image_path = $ARGV[0];

# face cascade bundled with OpenCV
my $classifier = Image::ObjectDetect->new('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml');

# run classifier
my @faces = $classifier->detect($image_path);

for my $face (@faces) {
	print join(', ', $face->{x}, $face->{y}, $face->{width}, $face->{height}), "\n";
}
