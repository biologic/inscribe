#!/usr/bin/perl
#--------------------------------------------------------------------------------
# makeImages
#
# Create SVG files and then .PNG files for Han characters
# See below for options - feed a flat text file of Unicode values through STDIN
# 
# Stylus, Copyright 2006-2008 Biologic Institute
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#--------------------------------------------------------------------------------

use strict;
use utf8;

use File::Copy;
use File::Path;
use File::Spec;

use FindBin;
use Getopt::Long;

# Path to Batik SVG rasterizer (see http://xmlgraphics.apache.org/batik/)
my $c_javaRasterizer = "java -jar $FindBin::Bin/../../../External/batik-1.6/batik-rasterizer.jar";

my %c_hTargets =
(
 'large' => 550,
 'medium' => 150,
 'small' => 60
);

my $c_strImageDir = '../images';

my @_arySizes;
my @_aryHan;
my $_fClean = 0;
my $_fSVG = 1;
my $_fImages = 1;

sub ensureDirectories
{
	mkdir($c_strImageDir);
	foreach my $strHan (@_aryHan)
	{
		mkdir($c_strImageDir . '/' . substr($strHan, 0, length($strHan)-3) . '000');
	}
}

sub optSizes
{
	my ($strOption, $strValue) = @_;
	$_arySizes[@_arySizes] = $strOption;
}

if (!GetOptions(
		 'large' => \&optSizes,
		 'medium' => \&optSizes,
		 'small' => \&optSizes,

		 'svg!' => \$_fSVG,
		 'images!' => \$_fImages,
	))
{
	print "ERROR: Incorrect arguments\n";
	exit(1);
}

my %hSizes = ();
@_arySizes = grep { ! $hSizes{$_} ++ } @_arySizes;
$_arySizes[@_arySizes] = 'large' if !scalar(@_arySizes);

while (<>)
{
	chomp;
	$_aryHan[@_aryHan] = $_;
}
print scalar(@_aryHan) . " characters to process\n";

&ensureDirectories;

my $c_strSVGFormat =
	"<?xml version='1.0' standalone='no'?>" .
	"<!DOCTYPE svg PUBLIC '-//W3C//DTD SVG 1.0//EN' 'http://www.w3.org/Graphics/SVG/1.0/DTD/svg10.dtd'>" .
	"<svg width='%dpx' height='%dpx' version='1.0' xmlns='http://www.w3.org/2000/svg'>" .
	"<text x='0' y='%d' font-family='Arial Unicode' font-size='%dpx' fill='black'>%s</text>" .
	"</svg>\n";
my $cHan = 0;
if ($_fSVG)
{
	foreach my $strHan (@_aryHan)
	{
		printf "Created $cHan SVG files...\n" if !(++$cHan % 100);
		my $strDir = $c_strImageDir . '/' . substr($strHan, 0, length($strHan)-3) . '000/';
		foreach my $strSize (@_arySizes)
		{
			my $nSize = $c_hTargets{$strSize};
			my $str = $strDir . $strHan . "-$strSize.svg";
			open(FILE, ">:utf8", $str) or print $!;
			printf FILE $c_strSVGFormat, $nSize, $nSize, int($nSize * 0.9), $nSize, chr(hex $strHan);
			close(FILE);
		}
	}
}

if ($_fImages)
{
	my $c_strTotalLine = '^.* transcode (\d+) SVG.*$';
	my $c_strConvertLine = '^Converting .*';
	my $c_strConvertSuccess = ' success$';
	foreach my $strSize (@_arySizes)
	{
		my @arySVG = map { $_ = $c_strImageDir . '/' . substr($_, 0, 1) . '000/' . $_ . "-$strSize.svg" } @_aryHan;
		my $cConverted = 0;

		open(RESULTS, "$c_javaRasterizer " . join(' ',@arySVG) . " |")
			or die "ERROR: Unable to start rasterizer";
		while (<RESULTS>)
		{
			if ($_ =~ /$c_strTotalLine/o)
			{
				print "Converting $1 files\n";
			}

			elsif ($_ =~ /$c_strConvertLine/o)
			{
				print "SVG Conversion failed: $_\n" if !($_ =~ /$c_strConvertSuccess/o);
				print "$cConverted files converted\n" if !(++$cConverted % 10);
			}
		}
		close(RESULTS);
	}
}
