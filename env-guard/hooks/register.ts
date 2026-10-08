import type { Register } from 'claude-code'

// .env, .env.local, config/.env.production — not .envrc or env.ts
const SECRET_FILE = /(^|[\/])\.env(\.[^\/]*)?$/

const refusal = (name: string, path: string) => ({
  deny: `${name}: ${path} holds secrets and is off limits.`,
})

export const register: Register = on => {
  for (const tool of ['Read', 'Edit', 'Write'] as const) {
    on('tool.call', { tool }, ($, e, next) =>
      SECRET_FILE.test(e.file_path) ? refusal($.plugin.name, e.file_path) : next(e),
    ).catch(($, e, next) =>
      next.called ? next(e) : { deny: `${$.plugin.name}: its guard failed.` },
    )
  }
}
