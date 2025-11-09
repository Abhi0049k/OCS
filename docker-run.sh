#!/bin/bash
# Docker run script for easy container management

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    print_error "Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is available
if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    print_error "Docker Compose is not available. Please install Docker Compose."
    exit 1
fi

# Set Docker Compose command
if command -v docker-compose &> /dev/null; then
    DOCKER_COMPOSE="docker-compose"
else
    DOCKER_COMPOSE="docker compose"
fi

# Default action
ACTION=${1:-"build-and-run"}

case $ACTION in
    "build")
        print_status "Building OCS Docker image..."
        docker build -t ocs-landing-page-builder .
        print_status "Build complete!"
        ;;
        
    "run")
        print_status "Running OCS container..."
        docker run -it --rm \
            --name ocs-app \
            -v "$(pwd)/outputs:/app/outputs" \
            -v "$(pwd)/logs:/app/logs" \
            -e GEMINI_API_KEY="${GEMINI_API_KEY:-}" \
            ocs-landing-page-builder
        ;;
        
    "build-and-run")
        print_status "Building and running OCS..."
        docker build -t ocs-landing-page-builder .
        docker run -it --rm \
            --name ocs-app \
            -v "$(pwd)/outputs:/app/outputs" \
            -v "$(pwd)/logs:/app/logs" \
            -e GEMINI_API_KEY="${GEMINI_API_KEY:-}" \
            ocs-landing-page-builder
        ;;
        
    "compose-up")
        print_status "Starting services with Docker Compose..."
        if [ ! -f .env ]; then
            print_warning "No .env file found. Creating one from .env.example..."
            cp .env.example .env
        fi
        $DOCKER_COMPOSE up -d
        print_status "Services started! Check 'docker-compose logs' for output."
        ;;
        
    "compose-down")
        print_status "Stopping Docker Compose services..."
        $DOCKER_COMPOSE down
        ;;
        
    "compose-logs")
        print_status "Showing Docker Compose logs..."
        $DOCKER_COMPOSE logs -f
        ;;
        
    "shell")
        print_status "Opening shell in OCS container..."
        docker run -it --rm \
            --name ocs-shell \
            -v "$(pwd)/outputs:/app/outputs" \
            -v "$(pwd)/logs:/app/logs" \
            -e GEMINI_API_KEY="${GEMINI_API_KEY:-}" \
            ocs-landing-page-builder /bin/bash
        ;;
        
    "clean")
        print_status "Cleaning up Docker resources..."
        docker system prune -f
        print_status "Cleanup complete!"
        ;;
        
    "help"|*)
        echo "OCS Docker Management Script"
        echo ""
        echo "Usage: $0 [ACTION]"
        echo ""
        echo "Actions:"
        echo "  build          - Build Docker image only"
        echo "  run            - Run container with current directory mounted"
        echo "  build-and-run  - Build and run (default)"
        echo "  compose-up     - Start with Docker Compose"
        echo "  compose-down   - Stop Docker Compose services"
        echo "  compose-logs   - Show Docker Compose logs"
        echo "  shell          - Open shell in container"
        echo "  clean          - Clean up Docker resources"
        echo "  help           - Show this help"
        echo ""
        echo "Environment Variables:"
        echo "  GEMINI_API_KEY - Your Gemini AI API key"
        echo ""
        echo "Examples:"
        echo "  $0 build"
        echo "  GEMINI_API_KEY=your-key $0 run"
        echo "  $0 compose-up"
        ;;
esac