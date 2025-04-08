# Specification

## Purpose

The purpose of this application is to be able to locally compress individual video files or directories with videos towards a target size (usually under 10mb). The goal is for it to be as **user-friendly** as possible, by hard-coding sensible defaults.

This project comes from the need to manage a collection of short gameplay clips, mostly around 30-40MB each. It’ll help save disk space and make it easier to keep important clips archived for longer.

## Planned Features

**Compression (cli)**

* Target size of 8mb
* Be able to specify the output file name format ( for ex. "{date}_compressed" )
* For directories - take an input and specify an output directory
* For files - take an input file and specify an output file
* Show progress
* For batch files, save progress to continue in case of interruption

**GUI**

* A minimalist interface
* Adjust settings like file name format & preset
* Select directories or files to be compressed
* Visually see the progress of current compression job

**Extension Ideas**

* Drag-n-drop videos to compress them, output files will be in some default user folder