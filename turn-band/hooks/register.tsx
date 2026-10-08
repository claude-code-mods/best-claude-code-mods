import { atom, read, update } from 'claude-code'
import type { Register } from 'claude-code'

import type { TurnStats } from '../types'

const last = atom({ plugin: 'turn-band', key: 'last' } as const, null)
const isHidden = atom({ plugin: 'turn-band', key: 'isHidden' } as const, false)

export const register: Register = on => {
  let tools = 0

  on('prompt.submit', ($, e, next) => {
    tools = 0
    return next(e)
  })

  on('tool.call', ($, e, next) => {
    tools += 1
    return next(e)
  })

  on('turn.complete', async ($, e, next) => {
    const stats: TurnStats = { seconds: Math.round(e.durationMs / 1000), tools }
    await update($, last, () => stats)
    return next(e)
  })

  on('ui.render', { component: 'AbovePrompt' }, async ($, e, next) => {
    const stats = await read($, last)
    if (e.props.hasSurvey || stats === null || (await read($, isHidden))) {
      return next(e)
    }

    const { Box, Button, Text } = $.ui.resolve(e)
    return (
      <Box>
        <Text dimColor>
          Last turn: {stats.seconds}s, {stats.tools} tool calls{' '}
        </Text>
        <Button key="hide" label="Hide" onPress={() => update($, isHidden, () => true)} />
      </Box>
    )
  })
}
