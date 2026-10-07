# cert-san-match

把主机名匹配到证书：SAN 里的精确项与通配项、单层通配、忽略大小写、SAN 优先于 CN，并按项建索引。只用 Python 标准库。

```
python3 -m unittest discover -s tests
python3 -m sanmatch --sample=wildcard
python3 -m sanmatch --sample=plain
python3 -m sanmatch --sample=cn
python3 -m sanmatch --sample=case
python3 -m sanmatch --sample=work
```

## 口径

- **精确**：SAN 里的 `dns:` 名称与主机名忽略大小写后完全相等。
- **通配**：`*.后缀` 只匹配正好一层标签，不匹配裸后缀本身，也不匹配多层。
- **IP**：`ip:` 项按字面比较，不参与通配。
- **CN 回退**：只有当 SAN 里没有任何 `dns:` 项时才看 CN。
- **索引**：精确项与通配项分别建索引。

## 不变量

- 通配项匹配的标签数正好比后缀多一个。
- SAN 里有 `dns:` 项时 CN 不参与判定。
- `scanned` 不随 SAN 项数乘查询次数放大：八百项查八百次的 `scanned` 不超过 6000。

## 输出契约

`match(cert, host)` 返回布尔。场景打印一行 JSON。
`--sample=work` 打印 `{"names": N, "scanned": N}`。
