# Deep Neuronal Filter (DNF)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6360675.svg)](https://doi.org/10.5281/zenodo.6360675)

## Prerequisites Libraries and packages

Installation instructions below are for Ubuntu Linux LTS and MacOS.

1) Install the IIR and FIR filter libraries

Linux: `sudo add-apt-repository ppa:berndporr/dsp`, Mac: `brew tap berndporr/dsp`

Linux: `sudo apt-get install iir1-dev`, Mac: `brew install iir` (https://github.com/berndporr/iir1)

Linux: `sudo apt-get install fir1-dev`, Mac: `brew install fir` (https://github.com/berndporr/fir1)

2) Install openCV library by running:

Linux: `sudo apt install libopencv-dev`, Mac: `brew install opencv`

3) Install boost library by running:

Linux: `sudo apt-get install libboost-all-dev`, Mac: is included in opencv

4) And make sure you have `cmake` installed.

## How to compile

Type:

```
cmake .
```
to create the makefile and then

```
make
```
to compile the library and the demos.

## Installation

```
sudo make install
```

## Documentation

 - Online: https://berndporr.github.io/deepNeuronalFilter/
 - PDF: https://github.com/berndporr/deepNeuronalFilter/blob/main/docs/pdf/refman.pdf

## Applications

 - eeg_filter: removes noise from EEG (release)
 - ecg_filter: removes noise from ECG (alpha version)
 - audio_filter: removes noise from audio (beta version)
