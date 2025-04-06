function createCounter() {
  let count = 0 // Private variable
  return {
    increment: function () {
      count += 1
      return count
    },
    decrement: function () {
      count -= 1
      return count
    },
    getValue: function () {
      return count
    },
  }
}

const counter1 = createCounter()
console.log(counter1.increment()) // 1
console.log(counter1.increment()) // 2
const counter2 = createCounter()
console.log(counter2.increment()) // 1
console.log(counter2.decrement()) // 0
