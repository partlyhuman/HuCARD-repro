# Partlyhuman changes

* Archived Ichigo's original post at https://github.com/partlyhuman/HuCARD-repro-gerbers/blob/master/original-post/
* Archived Ichigo's HuConv program to prepare images for flashing at https://github.com/partlyhuman/HuCARD-repro-gerbers/blob/master/HuCONV_v1.5/
* Created and added templates to https://github.com/partlyhuman/HuCARD-repro-gerbers/blob/master/prints/ of my design including
	* A vector file for cutting vinyl to mimic the UV protection coating
	* A PSD template for making replica HuCard stickers
	* A 3d print for risers
* Gathered the original gerbers into the https://github.com/partlyhuman/HuCARD-repro-gerbers/blob/master/gerbers/ directory

Please note that the development of this PCB and all credit aside from the prints goes to https://github.com/ichigobankai/. Their original license terms apply https://github.com/partlyhuman/HuCARD-repro-gerbers/blob/master/LICENSE.

Below these edits are the original readme.

---

# HuCARD
Hucard gerbers ready for fab.

Hucard thickness need to be around ~2.4mm

TSOP is on the bottom side

You need to add a 2nd layer (plastic for example) to ensure thickness as PBC tends to be 2mm at maximum.

TSOP can be :
- 39SF0x0 series (SST/Microchip short "32 pins") - up to 4Mbits / 512kB, 
- 29F0x0 series (AMD and other brands, "long" 32 pins) - up to 4Mbits / 512kB,
- 29F080 40 pins - 8Mbits / 1MB

TSOP can also be (re)flashed after soldering (/WE flash connected to /WE bus)

ICHIGO
