export type TurnStats = { seconds: number; tools: number }

declare module 'claude-code' {
  interface PluginState {
    'turn-band': { last: TurnStats | null; isHidden: boolean }
  }
}
