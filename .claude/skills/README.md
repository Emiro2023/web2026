# Claude Code skills

Vendored from [anthropics/skills](https://github.com/anthropics/skills) at commit
`33375500bcea98d610eb30ce10ac4e59b89c390d`. Claude Code loads each folder here as a
project skill automatically.

| Skill | Use it for |
| --- | --- |
| `frontend-design` | Building distinctive, production-grade web UIs |
| `webapp-testing` | Testing local web apps with Playwright |
| `web-artifacts-builder` | Multi-component HTML artifacts (React, Tailwind, shadcn/ui) |
| `theme-factory` | Applying ready-made color/font themes to pages and slides |
| `skill-creator` | Writing and evaluating new skills |

All of these are Apache 2.0 (see each folder's `LICENSE.txt`). The document skills
(`docx`, `pdf`, `pptx`, `xlsx`) are source-available rather than open source, so they
are not copied here. Install them as a plugin instead:

```
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
```

To update, re-copy the folders from a newer checkout of anthropics/skills.

## Engineering team skills (alirezarezvani/claude-skills)

The 34 skill folders from `engineering-team/skills/` in
[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills), vendored at
commit `19392f7a08264ed00486a251f5b2098321771f94`. MIT license: see
`LICENSE-claude-skills-MIT.txt`.

They cover architecture, frontend, backend, fullstack, QA, TDD, code review, DevOps,
cloud (AWS, Azure, GCP), security, incident response, data, ML and Stripe. Start from
`engineering-skills/SKILL.md` for an index.
