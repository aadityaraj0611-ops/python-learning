
import random


def generate_ip():
    """Generate a simulated IPv4 address."""
    return ".".join(str(random.randint(1, 254)) for _ in range(4))


def generate_packets(count):
    """Generate simulated network packets."""
    protocols = ["TCP", "UDP", "HTTP", "DNS"]
    packets = []

    for packet_id in range(1, count + 1):
        packet = {
            "id": packet_id,
            "source": generate_ip(),
            "destination": generate_ip(),
            "protocol": random.choice(protocols),
            "size": random.randint(40, 2000)
        }

        packets.append(packet)

    return packets


def display_packets(packets):
    """Display all packets."""
    if not packets:
        print("\nNo packets available.")
        return

    print("\n" + "-" * 85)
    print(f"{'ID':<8}{'SOURCE IP':<20}{'DESTINATION IP':<20}{'PROTOCOL':<15}{'SIZE (Bytes)':<15}")
    print("-" * 85)

    for packet in packets:
        print(
            f"{packet['id']:<8}"
            f"{packet['source']:<20}"
            f"{packet['destination']:<20}"
            f"{packet['protocol']:<15}"
            f"{packet['size']:<15}"
        )

    print("-" * 85)


def filter_packets(packets):
    """Filter packets by protocol."""
    protocol = input(
        "\nEnter protocol (TCP/UDP/HTTP/DNS): "
    ).strip().upper()

    if protocol not in ["TCP", "UDP", "HTTP", "DNS"]:
        print("Invalid protocol.")
        return

    filtered_packets = []

    for packet in packets:
        if packet["protocol"] == protocol:
            filtered_packets.append(packet)

    print(f"\nFound {len(filtered_packets)} {protocol} packet(s).")
    display_packets(filtered_packets)


def find_large_packets(packets):
    """Find packets larger than a specified size."""
    try:
        limit = int(input("\nEnter packet size limit in bytes: "))

        if limit < 0:
            print("Size cannot be negative.")
            return

        large_packets = []

        for packet in packets:
            if packet["size"] > limit:
                large_packets.append(packet)

        print(f"\nFound {len(large_packets)} packet(s) larger than {limit} bytes.")
        display_packets(large_packets)

    except ValueError:
        print("Please enter a valid number.")


def traffic_statistics(packets):
    """Display network traffic statistics."""
    if not packets:
        print("\nNo packets available for analysis.")
        return

    total_packets = len(packets)
    total_size = 0
    protocol_count = {
        "TCP": 0,
        "UDP": 0,
        "HTTP": 0,
        "DNS": 0
    }

    largest_packet = packets[0]
    smallest_packet = packets[0]

    for packet in packets:
        total_size += packet["size"]
        protocol_count[packet["protocol"]] += 1

        if packet["size"] > largest_packet["size"]:
            largest_packet = packet

        if packet["size"] < smallest_packet["size"]:
            smallest_packet = packet

    average_size = total_size / total_packets

    print("\n========== NETWORK TRAFFIC STATISTICS ==========")
    print(f"Total packets       : {total_packets}")
    print(f"Total data size     : {total_size} bytes")
    print(f"Average packet size : {average_size:.2f} bytes")

    print("\nProtocol Distribution:")

    for protocol, count in protocol_count.items():
        print(f"{protocol:<10}: {count}")

    print("\nLargest Packet:")
    print(f"Packet ID : {largest_packet['id']}")
    print(f"Size      : {largest_packet['size']} bytes")

    print("\nSmallest Packet:")
    print(f"Packet ID : {smallest_packet['id']}")
    print(f"Size      : {smallest_packet['size']} bytes")

    print("=" * 50)


def add_packet(packets):
    """Add a new simulated packet."""
    protocols = ["TCP", "UDP", "HTTP", "DNS"]

    print("\nAvailable protocols:", ", ".join(protocols))

    protocol = input("Enter protocol: ").strip().upper()

    if protocol not in protocols:
        print("Invalid protocol.")
        return

    try:
        size = int(input("Enter packet size in bytes: "))

        if size <= 0:
            print("Packet size must be greater than zero.")
            return

        packet = {
            "id": len(packets) + 1,
            "source": generate_ip(),
            "destination": generate_ip(),
            "protocol": protocol,
            "size": size
        }

        packets.append(packet)
        print("\nPacket added successfully!")

    except ValueError:
        print("Please enter a valid packet size.")


def main():
    print("=" * 50)
    print("       NETWORK PACKET ANALYZER SIMULATOR")
    print("=" * 50)

    try:
        count = int(input("\nHow many packets should be generated? "))

        if count <= 0:
            print("Please enter a number greater than zero.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    packets = generate_packets(count)

    print(f"\nSuccessfully generated {count} simulated packets!")

    while True:
        print("\n============== MAIN MENU ==============")
        print("1. Display all packets")
        print("2. Filter packets by protocol")
        print("3. Find unusually large packets")
        print("4. View network traffic statistics")
        print("5. Add a simulated packet")
        print("6. Exit")
        print("=======================================")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            display_packets(packets)

        elif choice == "2":
            filter_packets(packets)

        elif choice == "3":
            find_large_packets(packets)

        elif choice == "4":
            traffic_statistics(packets)

        elif choice == "5":
            add_packet(packets)

        elif choice == "6":
            print("\nThank you for using Network Packet Analyzer Simulator!")
            break

        else:
            print("\nInvalid choice. Please select between 1 and 6.")


if __name__ == "__main__":
    main()
