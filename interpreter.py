import sys

if len(sys.argv) < 2:
  raise Exception("No file given")

fn = sys.argv[1]
with open(fn, 'r') as file:
  li = ["".join(line.split()) for line in file]
li.insert(0, "#")

run = True
i = 0
bins = {}
ptr = 0
stack = []
while run:
  line = li[i]
  if line.startswith("#"):
    pass
  elif line.startswith(":"):
    i = int(line[1:])
  elif line.startswith("="):
    bins[ptr] = stack[-1] == ord(line[1:])
  elif line.startswith("~"):
    bins[ptr] = stack[-1] == int(line[1:])
  elif line.startswith("!"):
    bins[ptr] = not bins[ptr]
  elif line.startswith(">"):
    ptr -= 1
  elif line.startswith("<"):
    ptr += 1
  elif line.startswith("?"):
    if not bins[ptr]:
      i += 1
  elif line.startswith(";"):
    run = False
  elif line.startswith("]"):
    print(chr(stack[-1]), end='')
  elif line.startswith("}"):
    print(stack[-1], end='')
  elif line.startswith("|"):
    stack.append(ord(line[1]))
  elif line.startswith("("):
    stack.append(int(line[1:])%255)
  elif line.startswith("["):
    stack.append(ord(input("  char ) ")[0]))
  elif line.startswith("{"):
    stack.append(int(input(" ascii ) "))%255)
  elif line.startswith("+"):
    stack[-2] = (stack[-1] + stack[-2]) % 255
    stack.pop()
  elif line.startswith("-"):
    stack[-2] = (stack[-1] - stack[-2] + 255) % 255
    stack.pop()
  elif line.startswith("*"):
    stack[-2] = (stack[-1] * stack[-2]) % 255
    stack.pop()
  elif line.startswith("/"):
    stack[-2] = int(stack[-1] / stack[-2])
    stack.pop()
  elif line.startswith("%"):
    stack[-2] = stack[-1] % stack[-2]
    stack.pop()
  elif line.startswith("\\"):
    stack[-2], stack[-1] = stack[-1], stack[-2]
  elif line.startswith("&"):
    stack.append(stack[-1])
  elif line.startswith("^"):
    stack.pop()
  else:
    print("ERROR AT LINE ", i-1, "\n", line)
    raise Exception("unknown command")
  i += 1