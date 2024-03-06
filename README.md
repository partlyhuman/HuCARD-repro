# Partlyhuman changes

* Archived Ichigo's [original post](original-post/)
* Archived Ichigo's [HuConv program](HuCONV_v1.5/) to prepare images for flashing
* Created and added [templates](prints/) of my design including
	* A vector file for cutting vinyl to mimic the UV protection coating
	* A PSD template for making replica HuCard stickers
	* A 3d print for risers
* Gathered the original gerbers from root into a [gerbers folder](gerbers/)
* **NEW!** Added a [programming adapter](HuCard-TL866/) for use with the popular TL866 II programmer
* **In progress** Started to reverse engineer the gerbers into a Kicad project. Will probably relayout things so this isn't a shameless clone.

Please note that the development of this PCB and all credit aside from the prints goes to https://github.com/ichigobankai/. Their original [LICENSE](LICENSE) continues to apply.

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
