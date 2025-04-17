from collections import defaultdict
from google.cloud import asset_v1

def list_assets(project_id):
    client = asset_v1.AssetServiceClient()
    project_resource = f"projects/{project_id}"
    
    # Create request
    request = asset_v1.ListAssetsRequest(
        parent=project_resource,
        asset_types=None,  # You can specify asset types if needed
        content_type=asset_v1.ContentType.RESOURCE,
        page_size=100  # Adjust page size as necessary
    )
    
    # List assets and count asset types
    asset_counts = defaultdict(int)
    total_assets = 0
    try:
        response = client.list_assets(request=request)
        for page in response.pages:
            for asset in page.assets:
                asset_counts[asset.asset_type] += 1
                total_assets += 1
    except Exception as e:
        print(f"Error during asset listing: {e}")
    
    return asset_counts, total_assets

if __name__ == "__main__":
    project_id = ""  # Replace with your GCP project ID
    asset_counts, total_assets = list_assets(project_id)
    for asset_type, count in asset_counts.items():
        print(f"Asset Type: {asset_type}, Quantity: {count}")
    print(f"Total different asset types discovered: {len(asset_counts)}")
    print(f"Total assets discovered: {total_assets}")
