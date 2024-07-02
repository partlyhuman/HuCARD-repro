This is a fork of @ichigobankai's excellent [reproduction HuCards](https://github.com/ichigobankai/HuCARD-repro-gerbers).

The goals of this fork are:
1. Archive Ichigo's hard work so it's not lost
2. Add accessories I've developed while using Ichigo's designs

# Archival

* Gathered the original gerbers from root into a [gerbers folder](gerbers/)
	* Made some minor renames of drill files for better recognition by fabricators
* Archived Ichigo's [original post](original-post/)
* Archived Ichigo's [HuConv program](HuCONV_v1.5/) to prepare images for flashing

# Additions

* Created and added [templates](prints/) of my design including
	* A vector file for cutting vinyl to mimic the UV protection coating
	* A PSD template for making replica HuCard stickers
	* A 3d print for risers
* Added a [programming adapter](HuCard-TL866/) for use with the popular TL866 II programmer
* Contributed a [programming routine](https://github.com/sanni/cartreader/pull/977) to the Open Source Cart Reader

# Usage

You can fabricate the gerbers by uploading a zip to your favourite fabricator. Suggest using white soldermask and black silkscreen. Fabricate at 1.6mm thickness. Gold fingers, ENIG finish, and edge bevel (ideally front side only) are nice to haves.

Solder the appropriate 5V flash chip (SST39SF010, SST39SF020, SST39SF040, MX29F040, or MX29F080). You'll probably want at least the 4Mbit versions ending in 40, for 512KB games. Use flux and magnification to make your job easier.

Print the riser and glue. Print the sticker on sticker paper, cut to size and adhere. Cut the UV shape out of black vinyl with a Cricut or Silhouette or the like, and affix.

# Programming

Several options:

1. Use the [Open Source Cart Reader](https://github.com/sanni/cartreader) + a community-contributed [SNES-PCE adapter](https://github.com/sanni/cartreader/discussions/345#discussioncomment-3453888) + the [JT-Studio HuCARD connector](https://jt-studios.com/product/38pin-pc-engine-connector/). Compile with `PCE_ENABLED` and `FLASH_ENABLED`. 
2. You can use a [TL866 II](http://autoelectric.cn/EN/TL866_main.html) + the [programming adapter](HuCard-TL866/) from this repo + the [JT-Studio HuCARD connector](https://jt-studios.com/product/38pin-pc-engine-connector/).
3. You can preprogram the flash chips with a flash programmer and appropriate adapter, like the TL866 and TSOP adapter, before assembly.

# LICENSE

Please note that the development of this PCB and all credit aside from the prints goes to https://github.com/ichigobankai/. Their original [LICENSE](LICENSE) continues to apply.
