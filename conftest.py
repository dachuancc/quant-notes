# 放在仓库根，确保 pytest 在导入测试时把仓库根加入 sys.path，
# 这样 tests/ 里可以 `import scripts.check_links`。
