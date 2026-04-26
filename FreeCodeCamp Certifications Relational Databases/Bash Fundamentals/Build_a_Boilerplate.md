# Build a Boilerplate

## Context

This document summarizes the **Build a Boilerplate** workshop from the
freeCodeCamp Relational Databases Certification track.

The workshop was completed in **GitHub Codespaces** through the CodeRoad
extension. Because the original work happens inside a temporary Linux-based
Codespaces environment, this repository keeps a cleaned learning record instead
of raw copied tutorial prompts.

The goal of this note is to preserve the workshop flow in a professional way:
what was being practiced, which commands were used, why those commands mattered,
and what final project structure was produced.

## Workshop Goal

Build and organize a website boilerplate using only Bash commands.

The workshop focuses on:

- navigating a Linux file system
- inspecting directories and files
- creating files and folders from the terminal
- copying, moving, renaming, and deleting files
- using command flags
- working with hidden files
- validating project structure with `find`
- redirecting output into a file

## Environment

- Platform: freeCodeCamp Relational Databases Certification
- Workspace: GitHub Codespaces
- Tutorial runner: CodeRoad
- Shell: Bash
- Operating system context: Linux virtual machine

## Walkthrough

### 1. Start the Terminal and Confirm the Shell Works

The first step was to open a terminal in the Codespaces workspace and confirm
that commands could be executed.

```bash
echo hello terminal
pwd
ls
```

What this verifies:

- `echo` prints text to the terminal.
- `pwd` shows the current working directory.
- `ls` lists the contents of the current directory.

This establishes the basic workflow: run a command, observe the output, and use
the output to decide the next navigation step.

### 2. Navigate the Existing Workspace

After confirming the terminal worked, the next step was to move through the
existing CodeRoad workspace and inspect its contents.

```bash
cd freeCodeCamp
pwd
ls
cd test
pwd
ls
cd ..
ls
more package.json
clear
```

What this practices:

- `cd <directory>` moves into a directory.
- `cd ..` moves one level up.
- `more <file>` opens a file one screen at a time.
- `clear` resets the terminal display without changing files.

The key idea is that command-line navigation should be verified often with
`pwd` and `ls`, especially when working inside generated or unfamiliar
workspaces.

### 3. Explore Nested Project Dependencies

The workshop then moved into nested folders to practice reading deeper
directory structures.

```bash
cd node_modules
ls
ls -l
cd has
ls
more README.md
more LICENSE
clear
ls
cd src
pwd
ls
more index.js
cd ..
cd ..
cd ../..
```

What this practices:

- `ls -l` displays a detailed file listing.
- File names do not always need extensions to be valid files.
- `cd ../..` moves up two directory levels.
- Deep navigation should be followed by `pwd` or `ls` to avoid losing context.

This section is mainly exploratory. It shows how to inspect an existing project
without editing it.

### 4. Create the Boilerplate Workspace

The actual boilerplate work started by creating a new `website` directory.

```bash
mkdir website
cd website
ls
echo hello website
touch index.html
touch styles.css
touch index.js
touch .gitignore
ls
ls -a
```

What this creates:

- `index.html` for HTML structure
- `styles.css` for styling
- `index.js` for JavaScript behavior
- `.gitignore` as a hidden Git-related file

Important detail:

- `ls` does not show hidden files by default.
- `ls -a` shows hidden files such as `.gitignore`.

### 5. Create Placeholder Assets

The workshop then created placeholder image, font, and icon files to practice
file creation and later organization.

```bash
touch background.jpg
touch header.png
touch footer.jpeg
touch roboto.font
touch lato.font
touch menlo.font
touch CodeAlly.svg
touch CodeRoad.svg
touch freeCodeCamp.svg
ls
```

What this practices:

- `touch <filename>` creates an empty file.
- File extensions communicate intended file type.
- Creating files first makes the later move, copy, and rename steps easier to
  understand.

### 6. Organize Images

The first cleanup step was to place image files inside an `images` directory.

```bash
mkdir images
cp background.jpg images/
cd images
ls
cd ..
ls
rm background.jpg
cp header.png images/
cp footer.jpeg images/
cd images
ls
cd ..
rm header.png
rm footer.jpeg
ls
```

What this practices:

- `mkdir images` creates a dedicated image folder.
- `cp <file> <destination>` copies files.
- `rm <file>` deletes files.

The important workflow is to verify the copied files before removing the
original files.

### 7. Rename and Organize Fonts

The original font files used a generic `.font` extension. The workshop renamed
them to more realistic font extensions and moved them into a dedicated folder.

```bash
mv roboto.font roboto.woff
mv lato.font lato.ttf
mv menlo.font menlo.otf
ls
mkdir fonts
mv roboto.woff fonts/
mv lato.ttf fonts/
mv menlo.otf fonts/
find
```

What this practices:

- `mv <old_name> <new_name>` renames files.
- `mv <file> <directory>/` moves files.
- `find` displays the current folder tree recursively.

The key learning point is that `mv` handles both renaming and moving.

### 8. Move Source Files Into `client/src`

Next, the workshop introduced a more realistic frontend structure by moving
source files under `client/src`.

```bash
mkdir client
mkdir client/src
mv index.html client/src/
mv index.js client/src/
mv styles.css client/src/
find
find client
find -name index.html
find -name styles.css
find -name src
```

What this practices:

- Nested directories can be created by passing a path to `mkdir`.
- Files can be moved across folders using relative paths.
- `find -name <target>` searches for files or folders by name.

This step introduces structure validation: after moving files, search for them
instead of assuming they moved correctly.

### 9. Reorganize Assets Under `client/assets`

The assets were then reorganized under the `client/assets` directory to match a
cleaner frontend project layout.

```bash
cd client
mkdir assets
cd assets
mkdir images
cd images
touch background.jpg
cd ../../..
cd images
mv header.png ..
cd ..
find -name images
mv header.png client/assets/images/
mv images/footer.jpeg client/assets/images/
find
rm images/background.jpg
rmdir images
mkdir client/assets/icons
mv CodeAlly.svg client/assets/icons/
mv CodeRoad.svg client/assets/icons/
mv freeCodeCamp.svg client/assets/icons/
mkdir client/assets/fonts
touch client/assets/fonts/roboto-bold.woff
touch client/assets/fonts/roboto-light.woff
touch client/assets/fonts/lato-bold.ttf
touch client/assets/fonts/lato-light.ttf
find client/assets
rm -r fonts
ls
```

What this practices:

- Creating deeper asset folders.
- Moving files into nested destinations.
- Removing empty directories with `rmdir`.
- Removing non-empty directories with `rm -r`.

Safety note:

`rm -r` should only be used after checking the target directory. It removes a
directory and everything inside it recursively.

### 10. Add Project-Level Files and README Content

The boilerplate also needed common project-level files.

```bash
touch package.json
touch server.js
touch README.md
ls
echo "I made this boilerplate" >> README.md
more README.md
echo "from the command line" >> README.md
more README.md
echo "for the freeCodeCamp bash lessons" >> README.md
more README.md
```

What this practices:

- `>>` appends output to a file.
- `more README.md` verifies the file content after each append.
- Repeated verification helps prevent accidental overwrite.

Important distinction:

- `>` overwrites file content.
- `>>` appends to existing file content.

### 11. Rename and Copy the Completed Boilerplate

The final steps renamed the original project folder and copied it as a second
boilerplate instance.

```bash
cd ..
ls
mv website website-boilerplate
ls
cp -r website-boilerplate toms-website
ls
find toms-website
find website-boilerplate
clear
echo "goodbye terminal"
exit
```

What this practices:

- Renaming a directory with `mv`.
- Copying a directory recursively with `cp -r`.
- Validating copied directory structures with `find`.
- Ending a terminal session with `exit`.

## Expected Final Structure

```bash
project/
├── freeCodeCamp/
├── website-boilerplate/
│   ├── .gitignore
│   ├── README.md
│   ├── client/
│   │   ├── assets/
│   │   │   ├── fonts/
│   │   │   │   ├── lato-bold.ttf
│   │   │   │   ├── lato-light.ttf
│   │   │   │   ├── roboto-bold.woff
│   │   │   │   └── roboto-light.woff
│   │   │   ├── icons/
│   │   │   │   ├── CodeAlly.svg
│   │   │   │   ├── CodeRoad.svg
│   │   │   │   └── freeCodeCamp.svg
│   │   │   └── images/
│   │   │       ├── background.jpg
│   │   │       ├── footer.jpeg
│   │   │       └── header.png
│   │   └── src/
│   │       ├── index.html
│   │       ├── index.js
│   │       └── styles.css
│   ├── package.json
│   └── server.js
└── toms-website/
    └── [copy of website-boilerplate]
```

## Command Reference

| Command | Purpose |
| --- | --- |
| `pwd` | Print the current working directory. |
| `ls` | List visible files and directories. |
| `ls -a` | List all files, including hidden files. |
| `ls -l` | Show detailed file and directory information. |
| `cd <directory>` | Move into a directory. |
| `cd ..` | Move one directory level up. |
| `cd ../..` | Move two directory levels up. |
| `mkdir <directory>` | Create a directory. |
| `touch <file>` | Create an empty file. |
| `more <file>` | View file content one screen at a time. |
| `cp <file> <destination>` | Copy a file. |
| `cp -r <directory> <destination>` | Copy a directory recursively. |
| `mv <source> <destination>` | Move or rename a file or directory. |
| `rm <file>` | Remove a file. |
| `rm -r <directory>` | Remove a directory and its contents recursively. |
| `rmdir <directory>` | Remove an empty directory. |
| `find` | Display a recursive file tree from the current directory. |
| `find -name <target>` | Search for files or folders by name. |
| `echo <text>` | Print text to the terminal. |
| `echo <text> >> <file>` | Append text to a file. |
| `clear` | Clear the terminal display. |
| `exit` | Close the terminal session. |

## Key Takeaways

- Command-line work should be verified frequently with `pwd`, `ls`, and `find`.
- Hidden files such as `.gitignore` require `ls -a` to appear in listings.
- `mv` is used for both renaming and moving.
- Recursive commands such as `cp -r` and `rm -r` are powerful and should be used
  carefully.
- A professional project structure can be created entirely from Bash when each
  operation is checked before moving to the next step.
