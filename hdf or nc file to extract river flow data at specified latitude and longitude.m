clc;clear;

% Setting folder paths and latitude/longitude points  
folderPath = 'your path';  
% lat = 40.7128; % latitude  
% lon = -74.0060; % longitude  
% 
% % hdfinfo = h5info('your path');
% h5disp('your hdf name');
% data = h5read('your hdf name','/dis');
% lon = h5read('your hdf name','/lon');
% lat = h5read('your hdf name','/lat');
% [mlon,mlat] = meshgrid(lon,lat);
% mlon=mlon(:);
% mlat=mlat(:);
% lonlat=[mlon,mlat];

ncFiles = dir(fullfile(folderPath, '*.nc')); 

Row_indices=[];
Nearest_values=[];
Nearest_distances = [];
for i=1:32
    
k = 1; % Number of closest values found

% Calculate the distance of each point in A from a given latitude and longitude value
distances = sqrt((lonlat(:, 1) - A(i,1)).^2 + (lonlat(:, 2) - A(i,2)).^2);

% Find the index of the closest K distances
[~, indices] = mink(distances, k);

% Get the latitude, longitude, distance and corresponding line number of the closest value
nearest_values = lonlat(indices, :);
Nearest_values=[Nearest_values;nearest_values];
nearest_distances = distances(indices);
Nearest_distances = [Nearest_distances;nearest_distances];
row_indices = indices;
Row_indices=[Row_indices;row_indices];

end

% for iFile = 1:length(hdfFiles)  
%     data = h5read(hdfFiles(iFile).name,'/dis');
%     DATA = [];
%     for i = 1:size(data ,3)
%         size(data ,3)
%         a = data(:,:,i)';   
%         a = a(:);          
%       DATA = [DATA, a(Row_indices)];  
%     end
%     DATA = [Nearest_values,Nearest_distances,DATA];
%     csvFileName = strrep(hdfFiles(iFile).name,'hdf','csv');
%     csvwrite(csvFileName,DATA);
% end
for iFile = 1:length(ncFiles)  
    data = ncread(ncFiles(iFile).name,'dis');
    DATA = [];
    for i = 1:size(data ,3)
        a = data(:,:,i)';   
        a = a(:);          
      DATA = [DATA, a(Row_indices)];  
    end
    DATA = [Nearest_values,Nearest_distances,DATA];
    csvFileName = strrep(ncFiles(iFile).name,'nc','csv');
    csvwrite(csvFileName,DATA);
end