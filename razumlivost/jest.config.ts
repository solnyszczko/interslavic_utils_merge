export default {
  testRunner: 'jest-circus/runner',
  transform: {
    '\\.ts$': 'ts-jest'
  },
  testPathIgnorePatterns: [
    '/node_modules/',
    '/dist/',
    '/__e2e__/'
  ],
};
