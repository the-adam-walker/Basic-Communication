import spidev
import time


def __init__(spi):
    spi.mode = 0b00
    spi.max_speed_hz = 5000
    spi.bits_per_word = 8
    spi.loop = False
    spi.cshigh = True
    spi.lsbfirst = False
    spi.threewire = False


def BytesToHex(Bytes):
    return ''.join(["0x%02X " % x for x in Bytes]).strip()


def BytesToBinary(Bytes):
    return bin(Bytes[0]) 


def main():
    spi = spidev.SpiDev(0,0)
    __init__(spi)
    while True:
        #spi.writebytes([0x7E001010010013A200419AA517FFFE00006869D4])
        read = BytesToBinary(spi.readbytes(1))
        print(read)
	time.sleep(0.5)
    spi.close()


if __name__ == '__main__':
    main()
