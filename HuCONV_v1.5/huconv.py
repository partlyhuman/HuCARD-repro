#!/usr/bin/python

import os, sys, binascii, time    

if __name__ == "__main__":
        print "-------------------------------------------------------" 
        print "PCE ROM prepare for HuPROG / HuCARD by ICHIGO v1.5/2015"
        print "-------------------------------------------------------" 
        
	if len(sys.argv) < 2:
		print "Syntax should be %s <input file>" % os.path.basename(sys.argv[0])
		sys.exit()
	else:
# process basic checks
		try:
			input = open(sys.argv[1], "rb")
		except:
			print "Input file does not exist"
			sys.exit()
		try:
			filename = os.path.splitext(sys.argv[1])[0]
        		output = open(filename+"_huprog_[PCE].bin", "wb")
        		output_us = open(filename+"_huprog_[TG16].bin", "wb")
			output_txt = open(filename+"_huprog.txt", "w")


			
		except:
			print "Can't write output file"
			input.close()
			sys.exit()


# checks were ok, let's proceed with the real work
# reading input file to a byte array
                region_adr = 17;
                region_search = binascii.unhexlify('A9FF5301AD00102940')
                #print  "region_search %s" % region_search
                
		data = bytearray(input.read())
		region_adr_test = data.find(region_search)

		if region_adr_test == -1:
                        region_adr = 0; #no region
                else:        
                        region_adr = region_adr_test+9

                #print "find %s" % data.find(region_search)
	
                txt = time.strftime("%d-%m-%Y %H:%M:%S")
                output_txt.write(sys.argv[1]+'\n')
                output_txt.write('--------------------------\n')
                output_txt.write(txt+'\n')
                output_txt.write('--------------------------\n')
		print "ORIGINAL ROM (input)"
                output_txt.write('ORIGINAL ROM (input)\n')
               
                #region read
                if region_adr!= 0:
                        input.seek(region_adr, 0)
                        region = ord(input.read(1))
                else:
                        region = 0   

                if region == 0xf0:
                        txt = "REGION   : LOCK (0x%X)" % region
                        
                elif region == 0x80:
                        txt = "REGION   : FREE (0x%X)" % region

                elif region == 0:
                        txt = "REGION   : NO REGION"
                        
                else:
                        txt = "REGION   : UNKNOWN (0x%X)" % region

                print txt
                output_txt.write(txt+'\n')

                if region_adr != 0:
                        txt = "REG. ADDR: 0x%X" % region_adr
                        print txt
                        output_txt.write(txt+'\n')

                #verif 0x200 first bytes	
                verif_header = bytearray()
                verif_headerbis = bytearray()
                
                for i in range(0x200): verif_header.append(0x00)
                for i in range(0x200): verif_headerbis.append(0x00)
                for i in range(0x20, 0x30, 1): verif_header[i] = data[i] #skip 0xF0 first bytes
                for i in range(0x100, 0x110, 1): verif_headerbis[i] = data[i] #skip 0xF0 first bytes
                
		#print "verif sum : %s" % sum(verif_header)
		#print "verif sumbis : %s" % sum(verif_headerbis)
				
                if sum(verif_header) and sum(verif_headerbis) < 4080 : #between 1 and 4079
                        infos = "NO HEADER"
                        header = 0
                else:
                        infos = "HEADERED ROM FOUND !"
                        header = 0x200

                filesize = os.path.getsize(sys.argv[1]) - header
                print "FILESIZE : %s bytes" % (filesize+header)

                if filesize == 393216:
                        infos = infos + "\n           ROM MIRRORED"

                txt = "Infos+   : %s" % infos
                print txt
                output_txt.write(txt+'\n')

                if len(data)- header == 393216:
                        # init a 8Mb 0xFF bytearray
                        buffer = bytearray()
                        buffer_us = bytearray()
                        for i in range(filesize*2): buffer.append(0xFF)
                        for i in range(filesize*2): buffer_us.append(0xFF)
                        for i in range(0x40000): buffer[i] = data[i + header]                            #copy 0=>3FFFF	
                        for i in range(0x40000): buffer[(0x40000 + i)] = data[i + header]                #copy 0=>3FFFF to 40000	
                        for i in range(0x40000, 0x60000, 1): buffer[(0x40000 + i)] = data[i + header]    #copy 40000=>5FFFF to 80000
                else:
                        buffer = bytearray()
                        buffer_us = bytearray()
                        for i in range(filesize): buffer.append(0xFF)
                        for i in range(filesize): buffer_us.append(0xFF)
                        for i in range(filesize): buffer[i] = data[i + header]

                if region_adr:                               
                        buffer[region_adr] = 0x80 #REGION FREE
                
                if len(data) - header == 393216:
                        if region_adr:  
                                buffer[(0x40000 + region_adr)] = 0x80 #REGION FREE MIRRORED ROM

		
                # writing output file
		output.write(buffer)

                # JAP(normal) to US console
                # bit0 << 7
                # bit1 << 5
                # bit2 << 3
                # bit3 << 1             
                # bit4 >> 1
                # bit5 >> 3
                # bit6 << 5
                # bit7 >> 7

		for i in range (0, len(buffer_us)):
                        buffer_us[i] = (((buffer[i] & 0x1) << 7)+((buffer[i] & 0x2) << 5)+((buffer[i] & 0x4) << 3)+((buffer[i] & 0x8) << 1)+((buffer[i] & 0x10) >> 1)+((buffer[i] & 0x20) >> 3)+((buffer[i] & 0x40) >> 5)+((buffer[i] & 0x80) >> 7))
 
		output_us.write(buffer_us)
		
                input.close()

                output.close()
                output_us.close()
		
                print "----------------------------------------------------" 
                txt = "GENERATED ROM (output)"
                print txt
                output_txt.write('--------------------------\n')
                output_txt.write(txt+'\n')
                
                #region read
          	output = open(filename+"_huprog_[PCE].bin", "rb")

                #region read
                if region_adr!= 0:
                        output.seek(region_adr, 0)
                        region = ord(output.read(1))
                else:
                        region = 0   

                if region == 0xf0:
                        txt = "REGION   : LOCK (0x%X)" % region
                        
                elif region == 0x80:
                        txt = "REGION   : FREE (0x%X)" % region

                elif region == 0:
                        txt = "REGION   : NO REGION"
                        
                else:
                        txt = "REGION   : UNKNOWN (0x%X)" % region

                print txt
                output_txt.write(txt+'\n')

                filesize = os.path.getsize(filename+"_huprog_[PCE].bin")
                txt = "FILESIZE : %s bytes" % filesize
                print txt
                output_txt.write(txt+'\n')

                if header:
                        txt = "Infos+   : HEADER REMOVED"                
                        print txt
                        output_txt.write(txt+'\n')
                        
                print "----------------------------------------------------" 
                print "File successfully generated !"
                
        # close file handles
                output.close()
                output_txt.close()
                time.sleep(0.5)

