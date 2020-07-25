import json

FILENAME="incidents.json"

src_counter = dict()
uniq_dst = dict()
file_dst = dict()
with open(FILENAME) as file:
    data = json.load(file)
    for ticket in data["tickets"]:
        src_ip = ticket["src_ip"]
        dst_ip = ticket["dst_ip"]
        file_hash = ticket["file_hash"]
        if src_ip not in src_counter:
            src_counter[src_ip] = 0
            uniq_dst[src_ip] = set()
        src_counter[src_ip] += 1
        uniq_dst[src_ip].add(dst_ip)
        
        if file_hash not in file_dst:
            file_dst[file_hash] = set()
        file_dst[file_hash].add(dst_ip)


for src,count in src_counter.items():
    print()
    print("src {}\tcount {}\tuniq dst {}".format(src,count, len(uniq_dst[src])))
    for dst in uniq_dst[src]:
        print("\t",dst)

print()
num_uniq_dst = 0
num_ips = 0
for file_hash, dst_ips in file_dst.items():
    print("file {}\t{}".format(file_hash, dst_ips))
    num_uniq_dst += len(dst_ips)
    num_ips += 1

print()
print("Uniq dst ip per file {0:.2f}".format(num_uniq_dst/num_ips))
