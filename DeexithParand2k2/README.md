# My understanding on : Forking and PR Workflow

1. **Upstream Repository**: "Upstream" refers to the original repository maintained by project maintainers.

2. **Fork the Upstream Repo**: Manually create a fork of the upstream repository to have a copy under your GitHub profile.

3. **Clone the Repo**: Clone the forked repository to your local development environment to work on contributions.

4. **Make Contributions**:  Make code changes locally, commit them, and push to your forked repository.

5. **Create a Pull Request (PR)**: Manually create a PR from your forked repository using the "Compare & pull request" button on GitHub.

6. **Write Informative Comments**: Provide a clear PR description explaining the purpose of your changes and any relevant context.

7. **Maintainer Review and Feedback**: Expect project maintainers or reviewers to review your PR and provide feedback.

8. **Reupdate and Push Changes**: If requested, update your code locally, commit changes, and push them. The existing PR will automatically update.

9. **PR Approval and Merging**: Once maintainers approve, they'll merge your PR into the upstream repository.

10. **Delete Branch**: As a best practice, delete the branch used for the specific issue or feature after PR is merged.

11. **Create New Branches**: Create new branches for each issue/PR for organized and isolated development.

Following these steps ensures a smooth contribution workflow while contributing to open-source projects.

# Something extra I learnt while I learnt about forking a repo : Making a "git pull" from upstream repo to your forked repo

We `git pull` command to fetch changes from the upstream repository (the original repository you forked from) into your local branch. 

Steps to incorporate upstream changes into your branch and push them along with your other changes:

1. **Fetch Upstream Changes:**

   First, ensure that you have set the upstream repository as a remote in your local repository. You typically set this up once:

   ```bash
   git remote add upstream https://github.com/original/repo.git
   ```

   **NOTE:** Depicts an application, that presents where a remote is used in github.

   Replace the URL with the URL of the original repository.

2. **Fetch Upstream Changes:**

   Fetch the latest changes from the upstream repository:

   ```bash
   git fetch upstream
   ```

3. **Merge Upstream Changes:**

   Merge the fetched changes from the upstream repository into your local branch:

   ```bash
   git merge upstream/main
   ```

   Replace `main` with the name of the base branch in the upstream repository (often `main` or `master`).

4. **Resolve Conflicts (if any):**

   If there are conflicts between your changes and the upstream changes, Git will notify you. You'll need to manually resolve these conflicts by editing the affected files, committing the resolved changes, and then continuing the merge:

   ```bash
   git add .
   git commit -m "Resolved conflicts"
   git merge --continue
   ```

5. **Push Changes:**

   After resolving conflicts (if any), and ensuring that everything is in order, you can push both your changes and the upstream changes to your fork on GitHub:

   ```bash
   git push origin your-branch-name
   ```

This process allows you to keep your branch up-to-date with changes made in the upstream repository while still working on your own contributions. It's important to regularly fetch and merge upstream changes to minimize conflicts and keep your codebase aligned with the latest developments in the original project.
