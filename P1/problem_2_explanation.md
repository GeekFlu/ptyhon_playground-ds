# Find Files

## Design
- Using helper methods os.listdir and os.path.join we get for the current directory all the files and group them into files with the suffix and directories
## Time complexity
- The time complexity O(n), being n the directories and files we need to scan from parent to children directories
## Space Complexity
-  The Space complexity required is
    - Is linear O(n) where n is the directories and files matching the suffix
### Reference Links
- [Python path Documentation](https://docs.python.org/3/library/os.path.html)
