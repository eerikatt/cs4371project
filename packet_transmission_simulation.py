
import pandas as pd
import hmac
import hashlib

def verify_hmac(row, secret_key):
    """Verify the HMAC of a packet."""
    data = ', '.join(map(str, row.drop(labels=['HMAC']).values)).encode()
    computed_hmac = hmac.new(secret_key, data, hashlib.sha256).hexdigest()
    return computed_hmac == row['HMAC']

def simulate_packet_transmission(file_path, secret_key, output_file):
    """Simulate the transmission of valid packets and stopping of invalid packets."""
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Add verification results
    df['Valid'] = df.apply(lambda row: verify_hmac(row, secret_key), axis=1)

    # Log results
    for _, row in df.iterrows():
        if row['Valid']:
            print(f"Packet ID {row.name}: Transmitted")
        else:
            print(f"Packet ID {row.name}: Stopped")

    # Save results to a new file
    df.to_csv(output_file, index=False)
    print(f"Results saved to: {output_file}")

# Example usage
if __name__ == "__main__":
    # File path and shared secret key
    file_path = 'benign_with_hmac.csv'
    shared_key = b'thisisthekey'
    output_file = 'packet_results.csv'
    
    # Simulate transmission
    simulate_packet_transmission(file_path, shared_key, output_file)
