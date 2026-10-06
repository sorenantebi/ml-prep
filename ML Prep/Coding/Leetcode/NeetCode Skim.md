# NeetCode Skim

Every NeetCode 250 problem with **only your solution**, for quick review. This note builds itself from the problem notes (the code block you wrote in each one), so it is always up to date. Nothing to maintain.

Back to [[NeetCode 250]]. Needs the Dataview plugin with JavaScript queries enabled (Settings, Dataview, "Enable JavaScript Queries").

Change `ONLY_SOLVED` to `true` in the block below to hide problems you have not solved yet.

```dataviewjs
const ROOT = "ML Prep/Coding/Leetcode";
const ONLY_SOLVED = false;

const root = app.vault.getAbstractFileByPath(ROOT);
const folders = root.children
	.filter(f => f.children && /^\d\d /.test(f.name))
	.sort((a, b) => a.name.localeCompare(b.name));

let total = 0, solved = 0;
const parts = [];

for (const f of folders) {
	const hub = (await dv.io.load(`${f.path}/${f.name}.md`)) ?? "";
	const items = [...hub.matchAll(/^- \[( |x)\] (🟢|🟡|🔴) \[\[[^|\]]+\|([^\]]+)\]\]/gm)];
	const lines = [];
	let secSolved = 0;
	for (const [, done, dot, name] of items) {
		total++;
		const note = (await dv.io.load(`${f.path}/${name}/${name}.md`)) ?? "";
		const m = note.match(/```python\n([\s\S]*?)```/);
		const code = m ? m[1].trimEnd() : "";
		const tick = done === "x" ? " ✅" : "";
		if (code.trim()) {
			solved++; secSolved++;
			lines.push(`**${dot} [[${name}]]**${tick}\n\n\`\`\`python\n${code}\n\`\`\`\n`);
		} else if (!ONLY_SOLVED) {
			lines.push(`${dot} [[${name}]]${tick} · *not solved yet*\n`);
		}
	}
	parts.push(`## ${f.name.replace(/^\d+ /, "")} (${secSolved}/${items.length})\n\n${lines.join("\n")}`);
}

dv.paragraph(`**Solved: ${solved} / ${total}**\n\n` + parts.join("\n"));
```
