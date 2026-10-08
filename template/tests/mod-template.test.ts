import { describe, expect, test } from 'claude-code/testing'

describe('mod-template', () => {
  test('the command answers', async ($, on) => {
    on('session.start', ($, e) => ({ cwd: e.cwd }))
    on('command.register', ($, e) => ({ value: { command: e.name } }))
    await $.session.start({ cwd: '/tmp', surface: 'terminal', isInteractive: true })
    const answer = await $.command.run({
      command: 'mod-template',
      args: '',
      origin: { kind: 'composer' },
      presentation: { isFullscreen: false, columns: 120 },
    })
    expect(answer.text).toBe('Hello from mod-template.')
  })
})
