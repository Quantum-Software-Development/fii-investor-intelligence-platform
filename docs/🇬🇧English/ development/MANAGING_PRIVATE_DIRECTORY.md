# Managing the `private/` Directory

This document explains how to use the `private/` directory and why certain Git commands must be executed from the terminal rather than added to the `.gitignore` file.

<br><br>

## What is `.gitignore`?

The `.gitignore` file tells Git which files and directories **should not be tracked** by version control.

It contains only ignore rules, such as:

<br>

```gitignore
private/
.env
venv/
__pycache__/
```

<br>

The `.gitignore` file **does not execute commands**. Its sole purpose is to tell Git which files and directories should be ignored.

<br><br>

## Adding the `private/` Directory

If you want to store personal files, experiments, credentials, or any other content that should not be published in the repository, add the `private/` directory to your `.gitignore` file:

<br>

```bash
echo "private/" >> .gitignore
```

<br>

> [!TIP]
>
> ### What does this command do?
>
> * Appends the `private/` rule to the end of the `.gitignore` file.
> * From that point on, newly created files inside this directory will no longer be tracked by Git.

<br><br>

## When Isn't This Enough?

If the `private/` directory **has already been committed**, simply adding it to `.gitignore` will **not** stop Git from tracking it.

In this case, run:

<br>

```bash
git rm -r --cached private/
```

<br>

### What does this command do?

* Removes the directory from Git's index (staging area).
* Keeps all files intact on your local machine.
* Stops Git from tracking the directory without deleting any local files.

No local files are removed.

<br><br>

## Recording the Change

After removing the directory from version control, commit the change:

<br>

```bash
git commit -m "chore: stop tracking private directory"
```

<br>

This commit records that the directory will continue to exist locally but will no longer be tracked by the repository.

<br><br>

## Command Summary

<br>

| Command                         | Purpose                                                        |
| ------------------------------- | -------------------------------------------------------------- |
| `echo "private/" >> .gitignore` | Adds `private/` to the `.gitignore` file.                      |
| `git rm -r --cached private/`   | Stops tracking the directory without deleting the local files. |
| `git commit -m "..."`           | Saves the change to the repository history.                    |

<br><br>

## Best Practices

* Use `private/` for personal files, credentials, local experiments, and temporary work.
* Never store secrets (`.env`, API keys, tokens, passwords, etc.) in the repository.
* Keep the `.gitignore` file limited to **ignore rules only**.
* Always run Git commands from the terminal, never inside the `.gitignore` file.
