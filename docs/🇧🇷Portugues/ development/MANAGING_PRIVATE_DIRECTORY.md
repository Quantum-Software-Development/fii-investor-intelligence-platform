# Managing the `private/` Directory

The `.gitignore` file tells Git which files and folders should **not**
be tracked.

## Add `private/` to `.gitignore`

``` bash
echo "private/" >> .gitignore
```

This appends the `private/` directory to the `.gitignore` file so Git
ignores it in future.

## If `private/` Was Already Committed

``` bash
git rm -r --cached private/
```

This removes the directory from Git's index while keeping the files on
your local machine.

Then commit the change:

``` bash
git commit -m "chore: stop tracking private directory"
```

## Summary

-   `echo "private/" >> .gitignore` --- adds the rule to ignore the
    directory.
-   `git rm -r --cached private/` --- stops Git from tracking the
    directory without deleting local files.
-   `git commit ...` --- records the change in the repository history.

> These commands belong in your terminal or project documentation,
> **not** inside the `.gitignore` file.
