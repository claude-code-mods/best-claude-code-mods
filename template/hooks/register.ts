import type { Register } from 'claude-code'

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    await $.command.register({ name: 'mod-template', description: 'Say hello from mod-template' })
    return next(e)
  })

  on('command.run', { command: 'mod-template' }, () => ({ text: 'Hello from mod-template.' }))
}
