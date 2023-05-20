import struct

class RedstoneSynth:
    def __init__(self):
        self.GDSII = []

    def read_GDSII(self, filepath):
        datatype_size_map = {0x00: 1, 0x01: 1, 0x02: 2, 0x03: 4, 0x04: 4, 0x05: 8, 0x06: 1}
        record_type_map = { 0x00 : 'HEADER', 0x01 : 'BGNLIB', 0x02 : 'LIBNAME', 0x03 : 'UNITS', 0x04 : 'ENDLIB', 0x05 : 'BGNSTR', 0x06 : 'STRNAME', 0x07 : 'ENDSTR', 0x08 : 'BONDARY', 0x09 : 'PATH', 0x0A : 'SERF', 0x0B : 'AREF', 0x0C : 'TEXT', 0x0D : 'LAYER', 0x0E : 'DATATYPE', 0x0F : 'WIDTH', 0x10 : 'XY', 0x11 : 'ENDEL', 0x12 : 'SNAME', 0x13 : 'COLROW', 0x15 : 'NODE', 0x16 : 'TEXTTYPE',  0x17 : 'PRESENTATION',  0x19 : 'STRING',  0x1A : 'STRANS',  0x1B : 'MAG',  0x1C : 'ANGLE',  0x1F : 'REFLIBS',  0x20 : 'FONTS',  0x21 : 'PATHTYPE',  0x22 : 'GENERATIONS',  0x23 : 'ATTRATABLE',  0x26 : 'ELFLAGS',  0x2A : 'NODETYPE',  0x2B : 'PROPATTR',  0x2C : 'PROPVALUE',  0x2D : 'BOX',  0x2E : 'BOXTYPE',  0x2F : 'PLEX',  0x32 : 'TAPENUM',  0x33 : 'TAPECODE',  0x36 : 'FORMAT',  0x37 : 'MASK',  0x38 : 'ENDMASKS'}
           
        with open(filepath, mode='rb') as file_handle:
            while True:
                record_size = struct.unpack('>h', file_handle.read(2))[0] 
                file_handle.seek(0, 1)
                record_type = struct.unpack('>b', file_handle.read(1))[0]
                file_handle.seek(0, 1)
                record_datatype = struct.unpack('>b', file_handle.read(1))[0]
                file_handle.seek(0, 1)
                
                bytes = [] 
                for i in list(range(0, (record_size - 4) // datatype_size_map[record_datatype])):
                    bytes.append( file_handle.read(datatype_size_map[record_datatype]) )
                    file_handle.seek(0, 1)


                record_data = []
                if record_datatype == 0x02:
                    for i in list(range(0, (record_size - 4) // 2)):
                        record_data.append(struct.unpack('>h', bytes[i])[0] )

                if record_datatype == 0x03:
                    for i in list(range(0, (record_size - 4) // 4)):
                        record_data.append( struct.unpack('>l', bytes[i])[0] )

                if record_datatype == 0x04:
                    for i in list(range(0, (record_size - 4) // 4)):
                        record_data.append( struct.unpack('>f', bytes[i])[0] )

                if record_datatype == 0x05:
                    for i in list(range(0, (record_size - 4) // 8)):
                        record_data.append( struct.unpack('>d', bytes[i])[0] )

                if record_datatype == 0x06:
                    for i in list(range(0, (record_size - 4))):
                        char = struct.unpack('>c', bytes[i])[0].decode("utf-8") 
                        if char != '\x00':
                            record_data.append(char)

                if record_datatype == 0x00 or record_datatype == 0x01:
                    record = [record_type_map[record_type]]
                else:
                    record = [record_type_map[record_type], record_data]
                self.GDSII.append(record)

                if(record_type_map[record_type] == "ENDLIB"):
                    break
    
    def synthesize(self):
        return 


if __name__ == "__main__":
    s = RedstoneSynth()
    
    # s.read_GDSII(filepath = "test/and.gds")
    # print(s.GDSII)

    s.read_GDSII(filepath = "test/counter.gds")
    print(s.GDSII)