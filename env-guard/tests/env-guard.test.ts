import { describe, expect, test } from 'claude-code/testing'

describe('env-guard', () => {
  test('refuses an edit of a .env file', async ($, on) => {
    let ran = false
    on('tool.call', () => {
      ran = true
      return { result: 'edited' as never }
    })
    const answer = await $.tool.call({
      tool: 'Edit',
      file_path: '/repo/.env.local',
      old_string: 'A=1',
      new_string: 'A=2',
    })
    expect(answer.deny).toContain('/repo/.env.local')
    expect(ran).toBe(false)
  })

  test('lets other files through', async ($, on) => {
    let ran = false
    on('tool.call', () => {
      ran = true
      return { result: 'read' as never }
    })
    const answer = await $.tool.call({ tool: 'Read', file_path: '/repo/.envrc' })
    expect(answer.deny).toBeUndefined()
    expect(ran).toBe(true)
  })
})
