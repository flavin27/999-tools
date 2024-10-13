# A toolkit for editing binary files from Zero Escape: 9 Doors, 9 Persons, 9 Hours!

## About

This toolkit is a collection of tools for editing the bin files from the Nintendo DS game 9 Hours, 9 Persons, 9 Doors. The tools works just fine but can be improved to work with the 3ds sequel, Zero Escape: Virtue's Last Reward.

## Tools

* Text Extractor:
Extracts the text from the .fsb file in the scr folder. The text is stored in a .txt file separting the phrases by newlines. The text is not Shift-JIS encoded, so you don't need to worry about that.

* Text Injector(WIP):
Injects the text from a .txt file into the .fsb file in the scr folder. The text must be in the newline created by the `Text Extractor`. 

## Usage

Well i should create a makefile for this but i'm lazy so you need to compile the tools by yourself. The tools are written in C++ and uses the `std::filesystem` library, so you need to compile with the `-lstdc++fs` flag.

## Contributing

Feel free to contribute to this project. I'm not a C++ expert so any help is appreciated. As a said before, the tools can be improved to work with the 3ds sequel.

## License

This project has no financial purpose and is only for educational purposes and has no relation with Spike Chunsoft. The tools are licensed under the MIT License.
