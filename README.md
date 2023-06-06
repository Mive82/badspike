# Bad Apple on LEGO Spike Prime

This is a port of Bad Apple running on LEGO Spike Prime (45678) and Mindstorms Inventor (51515) (not tested) on stock legacy firmware (1.3.0.0 / 4.0.0.7).

Check out the video [Here](https://www.youtube.com/watch?v=nrx5CHRVuOc)

## How it works

The program reads the frames and audio data from the filesystem.  
The audio data is raw unsigned 16-bit PCM truncated to 12-bit at 16kHz sample rate,
and the video data is a byte stream where each byte is a value in range [0,9] that represents each pixel.
The brick reads the video data 25 bytes at a time and displays it.

The program is written in python using the reverse-enginered scratch api which you can check out [Here](https://github.com/azzieg/mindstorms-inventor).

## Copying the data

In order for the program to actually run, it needs to have the data copied to the brick's flash memory. 
Luckily, the flash is almost unused, as we have 31 out of 32 megabytes free.

To copy the data, use the `cp.py` script inside the data folder, copied from sanjayseshan's [spikeprime-tools](https://github.com/sanjayseshan/spikeprime-tools)
repository, to copy over the `audio` and `frames` files into the root `/` folder on the brick's filesystem.

- `./cp.py "frames"` - to copy the video frames
- `./cp.py "audio"` - to copy the audio

Note: the brick will probably reboot after each copy.

The brick seems to check its file system on every boot, so the boot time will increase after this.

## Running the program

In order to get the program on the brick, using the Spike APP won't work properly. 
Use the following process:  
- Open VSCode
- Download this extension [LEGO SPIKE Prime / MINDSTORMS Robot Inventor Extension](https://marketplace.visualstudio.com/items?itemName=PeterStaev.lego-spikeprime-mindstorms-vscode)
- Open the `badapple.py` file in VSCode.
- Upload the file to the brick using the `Python: Advanced` option