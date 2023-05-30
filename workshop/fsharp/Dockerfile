# syntax=docker/dockerfile:1.0.0-experimental
# **Build project**
# https://hub.docker.com/_/microsoft-dotnet
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
EXPOSE 80

WORKDIR /source

# Copy fsproj and restore all dependencies
COPY ./*.fsproj ./
RUN dotnet restore

# Copy source code and build / publish app and libraries
COPY . .
RUN dotnet publish -c release -o /app

# **Run project**
# Create new layer with runtime, copy app / libraries, then run dotnet
FROM mcr.microsoft.com/dotnet/aspnet:6.0
WORKDIR /app
COPY --from=build /app .
ENTRYPOINT ["dotnet", "project.dll"]
