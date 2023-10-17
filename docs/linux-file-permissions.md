# Linux file permissions

## Set File Access Control List

How much of your life have you waisted on file permissions? For me the answer is many. This is mostly due to the limited scope of the standard permissions, owner, group, everyone. If only I could add more users more easily for things like log forwarding and taking backups. Well, I can! Enter setfacl. It makes additional permissions, run like this:

    setfacl -R -d -m u:someuser:rx /some/folder/
    setfacl -R -m u:someuser:rx /some/folder/

You need both. One sets what will happen for new files and the other sets for existing files.

And relax, life just got that little bit easier. Ahhhhhhhhh :)
