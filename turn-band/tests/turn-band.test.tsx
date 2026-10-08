import { describe, expect, test } from 'claude-code/testing'

const BAND = { plugin: 'turn-band', component: 'AbovePrompt', props: { hasSurvey: false } } as const

describe('turn-band', () => {
  for (const surface of ['terminal', 'desktop'] as const) {
    test(`shows the last turn, and Hide hides it (${surface})`, async ($, on) => {
      on('ui.render', ($, e) => {
        const { Box } = $.ui.resolve(e)
        return <Box key="engine" />
      })
      on('tool.call', () => ({ result: 'ok' as never }))
      on('prompt.submit', ($, e) => ({ text: e.text }))
      on('turn.complete', ($, e) => ({ text: e.answer }))

      await $.prompt.submit({ text: 'go' } as never)
      await $.tool.call({ tool: 'Read', file_path: '/repo/a.ts' })
      await $.tool.call({ tool: 'Read', file_path: '/repo/b.ts' })
      await $.turn.complete({ answer: 'done', durationMs: 6400, isAborted: false, reason: 'answer' } as never)

      const ui = await $.ui.mount({ ...BAND, surface })
      expect((await ui.find({ text: 'Last turn: 6s, 2 tool calls ' }))).toBeDefined()

      await ui.press({ key: 'hide' })
      expect(await ui.find({ key: 'engine' })).toBeDefined()
    })
  }
})
