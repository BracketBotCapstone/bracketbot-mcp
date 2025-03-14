# server.py
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.utilities.types import Image
import httpx
from typing import Optional, Dict, Any, Union, List
import base64

# Create an MCP server
mcp = FastMCP("Multi-Robot Control MCP")

# Helper function to get robot API URL from port
def get_robot_api_url(port: int) -> str:
    """Get the API URL for a robot based on its port number"""
    return f"http://localhost:{port}"

# Define robot control tools that work with any robot port

@mcp.tool()
async def drive_forward(
    port: int = 8000,
    speed: float = 0.2, 
    duration: Optional[float] = None
) -> Dict[str, Any]:
    """
    Drive the robot forward at the specified speed.
    
    Args:
        port: Port number of the robot API (default: 8000)
        speed: Speed in meters per second (default: 0.2)
        duration: Duration in seconds (optional). If not provided, the robot will continue moving until stopped.
    
    Returns:
        Status message from the robot
    """
    robot_api_url = get_robot_api_url(port)
    params = {"speed": speed}
    if duration is not None:
        params["duration"] = duration
        
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{robot_api_url}/forward", params=params)
        response.raise_for_status()
        return response.json()

@mcp.tool()
async def drive_backward(
    port: int = 8000,
    speed: float = 0.2, 
    duration: Optional[float] = None
) -> Dict[str, Any]:
    """
    Drive the robot backward at the specified speed.
    
    Args:
        port: Port number of the robot API (default: 8000)
        speed: Speed in meters per second (default: 0.2)
        duration: Duration in seconds (optional). If not provided, the robot will continue moving until stopped.
    
    Returns:
        Status message from the robot
    """
    robot_api_url = get_robot_api_url(port)
    params = {"speed": speed}
    if duration is not None:
        params["duration"] = duration
        
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{robot_api_url}/backward", params=params)
        response.raise_for_status()
        return response.json()

@mcp.tool()
async def turn_left(
    port: int = 8000,
    speed: float = 1.2, 
    duration: Optional[float] = None
) -> Dict[str, Any]:
    """
    Turn the robot left at the specified angular speed.
    
    Args:
        port: Port number of the robot API (default: 8000)
        speed: Angular speed in radians per second (default: 1.2)
        duration: Duration in seconds (optional). If not provided, the robot will continue turning until stopped.
    
    Returns:
        Status message from the robot
    """
    robot_api_url = get_robot_api_url(port)
    params = {"speed": speed}
    if duration is not None:
        params["duration"] = duration
        
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{robot_api_url}/left", params=params)
        response.raise_for_status()
        return response.json()

@mcp.tool()
async def turn_right(
    port: int = 8000,
    speed: float = 1.2, 
    duration: Optional[float] = None
) -> Dict[str, Any]:
    """
    Turn the robot right at the specified angular speed.
    
    Args:
        port: Port number of the robot API (default: 8000)
        speed: Angular speed in radians per second (default: 1.2)
        duration: Duration in seconds (optional). If not provided, the robot will continue turning until stopped.
    
    Returns:
        Status message from the robot
    """
    robot_api_url = get_robot_api_url(port)
    params = {"speed": speed}
    if duration is not None:
        params["duration"] = duration
        
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{robot_api_url}/right", params=params)
        response.raise_for_status()
        return response.json()

@mcp.tool()
async def stop(port: int = 8000) -> Dict[str, Any]:
    """
    Stop all robot movement immediately.
    
    Args:
        port: Port number of the robot API (default: 8000)
    
    Returns:
        Status message from the robot
    """
    robot_api_url = get_robot_api_url(port)
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{robot_api_url}/stop")
        response.raise_for_status()
        return response.json()

@mcp.tool()
async def beep(
    port: int = 8000,
    frequency: float = 440.0,  # Hz (A4 note)
    duration: float = 1.0,     # seconds
    volume: float = 0.5,       # 0.0 to 1.0
) -> Dict[str, Any]:
    """
    Play a beep sound through the robot's speaker.
    
    Args:
        port: Port number of the robot API (default: 8000)
        frequency: Frequency in Hz (default: 440.0, which is the A4 note)
        duration: Duration in seconds (default: 1.0)
        volume: Volume between 0.0 and 1.0 (default: 0.5)
    
    Returns:
        Status message from the robot
    """
    robot_api_url = get_robot_api_url(port)
    params = {
        "frequency": frequency,
        "duration": duration,
        "volume": volume
    }
        
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{robot_api_url}/beep", params=params)
        response.raise_for_status()
        return response.json()

@mcp.tool()
async def drive(
    port: int = 8000,
    linear_velocity: float = 0.0,    # m/s
    angular_velocity: float = 0.0,   # rad/s
    duration: Optional[float] = None  # seconds
) -> Dict[str, Any]:
    """
    Control the robot with precise velocity values for advanced movement.
    
    Args:
        port: Port number of the robot API (default: 8000)
        linear_velocity: Linear velocity in m/s (forward/backward)
        angular_velocity: Angular velocity in rad/s (turning)
        duration: Duration in seconds (optional). If not provided, the robot will continue moving until stopped.
    
    Returns:
        Status message from the robot
    """
    robot_api_url = get_robot_api_url(port)
    json_data = {
        "linear_velocity": linear_velocity,
        "angular_velocity": angular_velocity
    }
    
    if duration is not None:
        json_data["duration"] = duration
        
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{robot_api_url}/drive", json=json_data)
        response.raise_for_status()
        return response.json()

@mcp.tool()
async def robot_status(port: int = 8000) -> Dict[str, Any]:
    """
    Get the status and available endpoints of the robot.
    
    Args:
        port: Port number of the robot API (default: 8000)
    
    Returns:
        Information about the robot's API and status
    """
    robot_api_url = get_robot_api_url(port)
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{robot_api_url}/")
        response.raise_for_status()
        return response.json()

@mcp.tool()
async def get_camera_image(
    port: int = 8000,
    format: str = "png",  # Format: jpeg, png
    quality: int = 90      # JPEG quality (1-100)
) -> Image:
    """
    Get the current camera image from the robot.
    
    Args:
        port: Port number of the robot API (default: 8000)
        format: Image format, either "jpeg" or "png" (default: "jpeg")
        quality: Image quality for JPEG format (1-100, default: 90)
    
    Returns:
        Image from the robot's camera
    """
    robot_api_url = get_robot_api_url(port)
    params = {
        "format": format,
        "quality": quality
    }
        
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{robot_api_url}/image", params=params)
        response.raise_for_status()
        
        # Get the image data
        image_data = response.content
        
        # Return as an Image object
        return Image(data=image_data, format=format)

@mcp.tool()
async def list_available_robots() -> List[Dict[str, Any]]:
    """
    List all available robots and their status.
    
    Returns:
        List of available robots with their port numbers and status
    """
    robots = [
        {"port": 8000, "name": "Robot 1"}, 
        {"port": 8001, "name": "Robot 2"}
    ]
    
    result = []
    for robot in robots:
        try:
            robot_api_url = get_robot_api_url(robot["port"])
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{robot_api_url}/", timeout=1.0)
                if response.status_code == 200:
                    robot_info = {
                        "port": robot["port"],
                        "name": robot["name"],
                        "status": "online",
                        "info": response.json()
                    }
                else:
                    robot_info = {
                        "port": robot["port"],
                        "name": robot["name"],
                        "status": f"error: {response.status_code}"
                    }
        except Exception as e:
            robot_info = {
                "port": robot["port"],
                "name": robot["name"],
                "status": f"offline: {str(e)}"
            }
            
        result.append(robot_info)
    
    return result

# Add resource to get information about a robot
@mcp.resource("robot://info/{port}")
async def get_robot_info(port: int = 8000) -> Dict[str, Any]:
    """Get information about a robot's capabilities"""
    robot_name = f"Robot (Port {port})"
    
    # Try to get actual robot name from API if available
    try:
        robot_api_url = get_robot_api_url(port)
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{robot_api_url}/")
            if response.status_code == 200:
                data = response.json()
                if "name" in data:
                    robot_name = data["name"]
    except:
        pass  # Use default name if API call fails
    
    return {
        "name": robot_name,
        "port": port,
        "capabilities": [
            "Movement: forward, backward, left, right",
            "Sound: beep at different frequencies",
            "Control: precise velocity control",
            "Vision: camera image capture"
        ],
        "api_endpoints": [
            "/forward - Move forward",
            "/backward - Move backward",
            "/left - Turn left",
            "/right - Turn right", 
            "/stop - Stop movement",
            "/beep - Play sound",
            "/drive - Precise movement control",
            "/image - Get camera image",
            "/image/base64 - Get base64 encoded camera image"
        ]
    }

# Run the server if executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(mcp.app, host="0.0.0.0", port=3000)